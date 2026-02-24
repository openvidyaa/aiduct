from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from datetime import datetime
import os

# Aeroseal brand colors
AEROSEAL_BLUE = colors.HexColor('#1e3a8a')
AEROSEAL_LIGHT_BLUE = colors.HexColor('#3b82f6')
AEROSEAL_GREEN = colors.HexColor('#10b981')
AEROSEAL_GRAY = colors.HexColor('#6b7280')

def generate_proposal_pdf(data, output_path):
    """Generate a professional Aeroseal proposal PDF"""

    # Create PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)

    # Container for PDF elements
    story = []

    # Get styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=AEROSEAL_BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=AEROSEAL_BLUE,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leading=14
    )

    # Cover Page
    story.append(Spacer(1, 1.5*inch))

    # Logo placeholder (you can add actual logo file later)
    story.append(Paragraph("🏠", ParagraphStyle('Logo', parent=title_style, fontSize=48)))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("AEROSEAL", title_style))
    story.append(Paragraph("Energy Savings Proposal", ParagraphStyle('Subtitle', parent=body_style,
                                                                     fontSize=18, textColor=AEROSEAL_LIGHT_BLUE,
                                                                     alignment=TA_CENTER)))
    story.append(Spacer(1, 0.5*inch))

    # Customer info box
    customer_info = f"""
    <para alignment="center" fontSize="14">
    <b>Prepared For:</b><br/>
    {data['customerName']}<br/>
    {data['address']}<br/>
    <br/>
    <b>Prepared By:</b><br/>
    {data['contractorName']}<br/>
    Certified Aeroseal Contractor<br/>
    <br/>
    <b>Date:</b> {data['date_generated']}
    </para>
    """
    story.append(Paragraph(customer_info, body_style))

    story.append(PageBreak())

    # Executive Summary
    story.append(Paragraph("Executive Summary", heading_style))
    story.append(Paragraph(data.get('executive_summary', ''), body_style))
    story.append(Spacer(1, 0.3*inch))

    # Key Highlights Table
    highlights_data = [
        ['Metric', 'Value'],
        ['Building Type', data['buildingType']],
        ['Building Size', f"{data['sqft']:,} sq ft"],
        ['Current Annual Energy Cost', f"${data['annual_energy_cost']:,.2f}"],
        ['Projected Annual Savings', f"${data['annual_savings']:,.2f}"],
        ['Savings Percentage', f"{data['expected_savings_pct']:.1f}%"],
        ['Simple Payback Period', f"{data['payback_years']:.1f} years"],
        ['10-Year Cumulative Savings', f"${data['ten_year_savings']:,.2f}"],
        ['CO₂ Reduction (Annual)', f"{data['co2_reduction_lbs']:,.0f} lbs"],
    ]

    highlights_table = Table(highlights_data, colWidths=[3*inch, 2.5*inch])
    highlights_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), AEROSEAL_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f3f4f6')]),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))

    story.append(highlights_table)
    story.append(PageBreak())

    # Problem Statement
    story.append(Paragraph("Current Situation & Opportunity", heading_style))

    problem_text = f"""
    Your {data['buildingType']} was built in {data['yearBuilt']} and is experiencing typical duct system inefficiencies common in buildings of this age. Based on our assessment, your duct system likely has approximately <b>{data['current_leakage_pct']:.0f}% leakage</b>, which is causing:
    <br/><br/>
    • Uneven temperatures throughout the building<br/>
    • Higher than necessary energy bills<br/>
    • Poor indoor air quality<br/>
    • Excessive dust and allergens<br/>
    • Overworked HVAC equipment<br/>
    <br/>
    Your current HVAC system, which is {data['hvacAge']} years old, is working harder than necessary to compensate for these leaks, resulting in an estimated annual energy cost of <b>${data['annual_energy_cost']:,.2f}</b>.
    """

    story.append(Paragraph(problem_text, body_style))
    story.append(Spacer(1, 0.3*inch))

    # Solution
    story.append(Paragraph("Our Solution: Aeroseal Duct Sealing", heading_style))

    solution_text = f"""
    Aeroseal's patented technology will seal your duct leaks from the inside out, dramatically reducing energy waste and improving comfort. We expect to achieve approximately <b>{data['expected_savings_pct']:.0f}% reduction in duct leakage</b>, resulting in:
    <br/><br/>
    • <b>${data['annual_savings']:,.2f}</b> in annual energy savings<br/>
    • Improved comfort and temperature consistency<br/>
    • Better indoor air quality<br/>
    • Extended HVAC equipment lifespan<br/>
    • Reduced carbon footprint<br/>
    """

    story.append(Paragraph(solution_text, body_style))
    story.append(PageBreak())

    # Financial Analysis
    story.append(Paragraph("Financial Analysis", heading_style))

    # Cost breakdown table
    cost_data = [
        ['Item', 'Amount'],
        ['Aeroseal Duct Sealing Service', f"${data['project_cost']:,.2f}"],
        ['Less: Available Rebates/Incentives', f"TBD*"],
        ['Net Investment', f"${data['project_cost']:,.2f}"],
        ['', ''],
        ['Annual Energy Savings', f"${data['annual_savings']:,.2f}"],
        ['Simple Payback Period', f"{data['payback_years']:.1f} years"],
        ['10-Year Return on Investment', f"${data['ten_year_savings']:,.2f}"],
        ['ROI Percentage (10 years)', f"{(data['ten_year_savings']/data['project_cost']*100):.0f}%"],
    ]

    cost_table = Table(cost_data, colWidths=[3.5*inch, 2*inch])
    cost_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), AEROSEAL_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#f3f4f6')),
        ('LINEABOVE', (0, 4), (-1, 4), 2, colors.black),
        ('FONTNAME', (0, 6), (-1, 8), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 6), (-1, 8), colors.HexColor('#dcfce7')),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))

    story.append(cost_table)
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("<i>* We will research available federal, state, and utility rebates specific to your location.</i>",
                          ParagraphStyle('Footnote', parent=body_style, fontSize=9, textColor=AEROSEAL_GRAY)))

    story.append(Spacer(1, 0.3*inch))

    # 10-year savings projection
    story.append(Paragraph("10-Year Savings Projection", ParagraphStyle('Subheading',
                                                                        parent=heading_style,
                                                                        fontSize=14,
                                                                        textColor=AEROSEAL_LIGHT_BLUE)))

    projection_data = [['Year', 'Cumulative Savings']]
    cumulative = 0
    for year in range(1, 11):
        cumulative += data['annual_savings']
        projection_data.append([f"Year {year}", f"${cumulative:,.2f}"])

    projection_table = Table(projection_data, colWidths=[1.5*inch, 2*inch])
    projection_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), AEROSEAL_LIGHT_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f3f4f6')]),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))

    story.append(projection_table)
    story.append(PageBreak())

    # Environmental Impact
    story.append(Paragraph("Environmental Impact", heading_style))
    story.append(Paragraph(data.get('environmental_impact', ''), body_style))
    story.append(Spacer(1, 0.3*inch))

    # Environmental stats
    env_data = [
        ['Environmental Benefit', 'Annual Impact'],
        ['CO₂ Reduction', f"{data['co2_reduction_lbs']:,.0f} lbs"],
        ['Equivalent Trees Planted', f"{data['co2_reduction_lbs']/48:.0f} trees"],
        ['10-Year CO₂ Prevention', f"{data['co2_reduction_lbs']*10/2000:.1f} tons"],
    ]

    env_table = Table(env_data, colWidths=[3*inch, 2.5*inch])
    env_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), AEROSEAL_GREEN),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecfdf5')]),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))

    story.append(env_table)
    story.append(PageBreak())

    # The Aeroseal Process
    story.append(Paragraph("The Aeroseal Process", heading_style))
    story.append(Paragraph(data.get('process_description', ''), body_style))
    story.append(Spacer(1, 0.3*inch))

    # Timeline
    timeline_text = """
    <b>Typical Project Timeline:</b><br/>
    • <b>Day 1:</b> Pre-sealing inspection and preparation (1-2 hours)<br/>
    • <b>Day 2-3:</b> Aeroseal sealing process (4-8 hours depending on system size)<br/>
    • <b>Day 3:</b> Post-sealing verification and certification<br/>
    • <b>Completion:</b> Receive detailed before/after report and warranty documentation<br/>
    """
    story.append(Paragraph(timeline_text, body_style))

    story.append(PageBreak())

    # About Aeroseal
    story.append(Paragraph("About Aeroseal Technology", heading_style))

    about_text = """
    Aeroseal is the world's leading duct sealing technology, developed in partnership with the U.S. Department of Energy at Lawrence Berkeley National Laboratory. Our patented system has been proven in over <b>300,000 homes and buildings worldwide</b>.
    <br/><br/>
    <b>Why Aeroseal?</b><br/>
    • Proven, patented technology with 20+ years of field results<br/>
    • Non-toxic, water-based sealant safe for all occupants<br/>
    • Computer-verified results with certification<br/>
    • 10-year warranty on sealed ductwork<br/>
    • Reduces duct leakage by up to 90%<br/>
    • No invasive demolition or ductwork access required<br/>
    <br/>
    <b>Industry Recognition:</b><br/>
    • U.S. Department of Energy technology<br/>
    • Featured on PBS, HGTV, and major media outlets<br/>
    • Recommended by building scientists and energy auditors<br/>
    • Meets or exceeds all building code requirements<br/>
    """

    story.append(Paragraph(about_text, body_style))
    story.append(PageBreak())

    # Next Steps
    story.append(Paragraph("Next Steps", heading_style))

    next_steps_text = f"""
    We're excited to help you achieve significant energy savings, improved comfort, and a reduced environmental footprint.
    To proceed with this project:
    <br/><br/>
    <b>1. Review this proposal</b> and contact us with any questions<br/>
    <b>2. Schedule your Aeroseal service</b> at a convenient time<br/>
    <b>3. We'll handle all details</b> including rebate applications and permitting<br/>
    <br/>
    <b>Contact Information:</b><br/>
    {data['contractorName']}<br/>
    Certified Aeroseal Contractor<br/>
    Email: {data['customerEmail']}<br/>
    <br/>
    This proposal is valid for 30 days from {data['date_generated']}.
    <br/><br/>
    We look forward to working with you to transform your building's energy efficiency!
    """

    story.append(Paragraph(next_steps_text, body_style))

    story.append(Spacer(1, 0.5*inch))

    # Signature block
    signature_data = [
        ['Authorized By:', ''],
        ['', ''],
        ['Signature: ___________________', f"Date: {data['date_generated']}"],
        ['', ''],
        [f"{data['contractorName']}", ''],
        ['Certified Aeroseal Contractor', ''],
    ]

    signature_table = Table(signature_data, colWidths=[3*inch, 2.5*inch])
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    story.append(signature_table)

    # Build PDF
    doc.build(story)

    return output_path
