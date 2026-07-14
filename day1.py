class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = {}   

    def add_grade(self, subject, marks):
        """Add or update a grade for a subject"""
        

    def calculate_average(self):
        """Return average of all grades"""
       

    def display_report_card(self):
        """Print name, roll no, all subjects+marks, and average"""
       
        pass


# --- Test your class here ---
s1 = Student("Harry", 1)
s1.add_grade("Python", 88)
s1.add_grade("Maths", 92)
s1.add_grade("Chemistry", 75)
s1.display_report_card()