from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from datetime import datetime
from proposal_generator import generate_proposal_pdf

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/api/generate-proposal', methods=['POST'])
def generate_proposal():
    try:
        data = request.json

        # Validate required fields
        required_fields = ['address', 'buildingType', 'sqft', 'yearBuilt', 'hvacAge',
                          'hvacType', 'summerBill', 'winterBill', 'ductLocation',
                          'customerName', 'customerEmail', 'contractorName']

        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Calculate energy savings and generate proposal content using AI
        proposal_data = calculate_energy_savings(data)

        # Generate PDF
        pdf_filename = f"aeroseal_proposal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf_path = os.path.join('proposals', pdf_filename)

        # Create proposals directory if it doesn't exist
        os.makedirs('proposals', exist_ok=True)

        generate_proposal_pdf(proposal_data, pdf_path)

        # Return success response
        return jsonify({
            'success': True,
            'pdf_url': f'/download/{pdf_filename}',
            'stats': {
                'annual_savings': proposal_data['annual_savings'],
                'payback_years': proposal_data['payback_years'],
                'co2_reduction': proposal_data['co2_reduction_lbs']
            }
        })

    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join('proposals', filename)
        return send_file(file_path, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': 'File not found'}), 404

def calculate_energy_savings(data):
    """Use AI to calculate energy savings and generate proposal content"""

    # Calculate average annual energy bill
    avg_monthly_bill = (float(data['summerBill']) + float(data['winterBill'])) / 2
    annual_energy_cost = avg_monthly_bill * 12

    # Create prompt for AI to calculate savings
    prompt = f"""
You are an energy efficiency expert analyzing a building for duct sealing with Aeroseal technology.

Building Details:
- Type: {data['buildingType']}
- Size: {data['sqft']} sq ft
- Year Built: {data['yearBuilt']}
- HVAC Age: {data['hvacAge']} years
- HVAC Type: {data['hvacType']}
- Average Summer Bill: ${data['summerBill']}
- Average Winter Bill: ${data['winterBill']}
- Annual Energy Cost: ${annual_energy_cost:.2f}
- Duct Location: {data['ductLocation']}
- Known Issues: {data.get('knownIssues', 'None specified')}

Based on industry research:
- Aeroseal duct sealing typically reduces HVAC energy loss by 20-30%
- Older buildings (pre-2000) often have 25-40% duct leakage
- HVAC systems account for ~40% of total energy usage in buildings

Please calculate and provide:
1. Estimated current duct leakage percentage (based on building age and symptoms)
2. Expected energy savings percentage after Aeroseal treatment
3. Annual energy cost savings in dollars
4. Estimated project cost (typical range: $1,500-$5,000 for residential, $5,000-$25,000 for commercial)
5. Simple payback period in years
6. 10-year cumulative savings
7. CO2 reduction in pounds per year (assume 1.5 lbs CO2 per kWh, estimate kWh from energy bills)
8. A compelling 2-3 sentence value proposition for this specific customer

Return your response as a valid JSON object with these exact keys:
{{
  "current_leakage_pct": number,
  "expected_savings_pct": number,
  "annual_savings": number,
  "project_cost": number,
  "payback_years": number,
  "ten_year_savings": number,
  "co2_reduction_lbs": number,
  "value_proposition": "string"
}}

Only return the JSON, no additional text.
"""

    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert energy efficiency calculator. Always respond with valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        # Parse AI response
        ai_result = json.loads(response.choices[0].message.content)

        # Ensure all numeric values are floats (AI might return strings)
        ai_result['current_leakage_pct'] = float(ai_result.get('current_leakage_pct', 30))
        ai_result['expected_savings_pct'] = float(ai_result.get('expected_savings_pct', 25))
        ai_result['annual_savings'] = float(ai_result.get('annual_savings', annual_energy_cost * 0.25))
        ai_result['project_cost'] = float(ai_result.get('project_cost', 3000))
        ai_result['payback_years'] = float(ai_result.get('payback_years', 3.5))
        ai_result['ten_year_savings'] = float(ai_result.get('ten_year_savings', annual_energy_cost * 0.25 * 10))
        ai_result['co2_reduction_lbs'] = float(ai_result.get('co2_reduction_lbs', 5000))

        # Combine input data with AI calculations
        proposal_data = {
            **data,
            **ai_result,
            'annual_energy_cost': annual_energy_cost,
            'date_generated': datetime.now().strftime('%B %d, %Y')
        }

        # Generate additional content using AI
        proposal_data['executive_summary'] = generate_executive_summary(proposal_data)
        proposal_data['process_description'] = get_aeroseal_process_description()
        proposal_data['environmental_impact'] = generate_environmental_impact(proposal_data)

        return proposal_data

    except Exception as e:
        print(f"AI Error: {str(e)}")
        # Fallback to conservative estimates if AI fails
        return {
            **data,
            'current_leakage_pct': 30,
            'expected_savings_pct': 25,
            'annual_savings': annual_energy_cost * 0.25,
            'project_cost': 3000 if data['buildingType'] == 'Single Family Home' else 15000,
            'payback_years': 3.5,
            'ten_year_savings': annual_energy_cost * 0.25 * 10,
            'co2_reduction_lbs': 5000,
            'value_proposition': f"Aeroseal duct sealing can reduce your energy costs by an estimated 25%, saving approximately ${annual_energy_cost * 0.25:,.0f} annually while improving comfort and air quality.",
            'annual_energy_cost': annual_energy_cost,
            'date_generated': datetime.now().strftime('%B %d, %Y'),
            'executive_summary': "Professional energy efficiency analysis",
            'process_description': get_aeroseal_process_description(),
            'environmental_impact': f"Reduce your carbon footprint by approximately 5,000 lbs of CO2 annually."
        }

def generate_executive_summary(data):
    """Generate executive summary using AI"""
    # Convert to float to ensure proper formatting
    annual_savings = float(data['annual_savings'])
    payback_years = float(data['payback_years'])
    co2_reduction = float(data['co2_reduction_lbs'])

    prompt = f"""
Create a compelling executive summary (2-3 paragraphs) for an Aeroseal duct sealing proposal with these highlights:
- Building: {data['buildingType']}, {data['sqft']} sq ft
- Annual savings: ${annual_savings:.0f}
- Payback: {payback_years:.1f} years
- CO2 reduction: {co2_reduction:.0f} lbs/year

Make it professional, benefit-focused, and persuasive. Focus on comfort, savings, and environmental impact.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional proposal writer for Aeroseal."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except:
        return f"This proposal outlines a comprehensive duct sealing solution for your {data['buildingType']}. Through Aeroseal's proven technology, we project annual energy savings of ${annual_savings:.0f}, with a payback period of {payback_years:.1f} years. Beyond financial savings, you'll experience improved comfort, better indoor air quality, and a significant reduction in your carbon footprint."

def generate_environmental_impact(data):
    """Generate environmental impact description"""
    co2_lbs = float(data['co2_reduction_lbs'])
    trees_equivalent = co2_lbs / 48  # One tree absorbs ~48 lbs CO2/year

    return f"By sealing your duct system, you'll prevent approximately {co2_lbs:.0f} pounds of CO2 from entering the atmosphere each year. This is equivalent to planting {trees_equivalent:.0f} trees or taking a car off the road for {co2_lbs/11000:.1f} months. Over 10 years, your cumulative environmental impact equals {co2_lbs*10/2000:.1f} tons of CO2 prevented."

def get_aeroseal_process_description():
    """Return standard Aeroseal process description"""
    return """
Aeroseal is a patented, proven technology that seals duct leaks from the inside out:

1. PREPARATION: All registers are temporarily sealed, and the system is prepared for sealing.

2. PRESSURIZATION: The duct system is pressurized with clean, conditioned air.

3. AEROSOL INJECTION: Non-toxic, water-based aerosol sealant particles are injected into the ductwork.

4. AUTOMATED SEALING: Particles seek out and seal leaks automatically, bonding to the edges of holes and gaps.

5. VERIFICATION: Computer software monitors the entire process, providing before-and-after leakage measurements.

6. CERTIFICATION: You receive a certificate showing exactly how much leakage was eliminated.

The entire process typically takes 4-8 hours and requires no invasive demolition or ductwork access. Aeroseal has sealed over 300,000 buildings worldwide with proven, lasting results.
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
