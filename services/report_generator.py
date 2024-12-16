from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from models import Person
import arabic_reshaper
from bidi.algorithm import get_display

class ReportGenerator:
    def __init__(self, output_path):
        self.output_path = output_path
        self.styles = getSampleStyleSheet()
    
    def _reshape_arabic(self, text):
        """Reshape Arabic text for proper rendering"""
        reshaped_text = arabic_reshaper.reshape(str(text))
        return get_display(reshaped_text)
    
    def generate_population_report(self):
        """Generate detailed population report"""
        doc = SimpleDocTemplate(
            self.output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Prepare story elements
        story = []
        
        # Add title
        title = Paragraph(
            self._reshape_arabic("تقرير التعداد السكاني"),
            self.styles['Heading1']
        )
        story.append(title)
        
        # Add statistics
        stats = [
            ["الإجمالي", Person.query.count()],
            ["ذكور", Person.query.filter_by(gender='male').count()],
            ["إناث", Person.query.filter_by(gender='female').count()],
            ["متزوجون", Person.query.filter_by(marital_status='married').count()]
        ]
        
        stats_table = Table(stats)
        stats_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.green),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(stats_table)
        
        # Build and save the PDF
        doc.build(story)
        
    def generate_age_distribution_report(self):
        """Generate age distribution report"""
        # Implementation for age distribution report
        pass