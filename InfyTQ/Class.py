class Instructor:
    def __init__(self, name, feed, xp, skill):
        self.instructor_name = name
        self.avg_feedback = feed
        self.experience = xp
        self.technology_skill = skill

    def check_eligibility (self):
            if ((self.experience>=3 and self.avg_feedback>=4.5) or (self.experience<=3 and self.avg_feedback>=4)):
                print "Eligible"
            else:
                print "NOT Eligible"
    def allocate_course(skill):
        for i in self.experience:
            if self.experience=='C++' or self.experience=='Java':
                return True

p1 = Instructor('Anmol', 4.6, 4, ['C++', 'Java'])
p1.check_eligibility()
