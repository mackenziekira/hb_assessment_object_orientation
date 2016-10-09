"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    1) Abstraction: The inner machinery of how something is done is hidden away/compartmentalized, so if a person wants to use a class/its information/its methods, the person doesn't have to know how they are handled internally, they just have to know about the inputs and outputs, and what attributes and methods are available to them as a programmer.
    2) Polymorphism: With subclasses and the possibility of instance attributes, you can easily make similar types of 'things' that have slightly different/unique attributes and methods without having to copy and paste the same code in a bunch of places, but rather by referencing a single class that contains in one place the information the subclasses or instances share.
    3) Encapsulation: Information/data (attributes) is bundled with specific stuff you can do to that information (methods). 

2. What is a class?
    
    A class is a grouping of attributes and methods that will be shared either by instances created from that class, or inherited by subclasses beneath that class.

3. What is an instance attribute?

    An instance attribute is an attribute that exists on that particular instance of a class. They can be set during instantiation, by including them in the init method, or they can be added once the class has been instantiated. If it shares a name with a class attribute from the class from which the instance was derived, the instance attribute would take precedence over the class attribute or any parent class attribute by the same name when Python is looking for the value belonging to the attribute.

4. What is a method?

    A method is a function that lives with a class and is accessible to all of the class's subclasses and all of the class's instances. It is not a function that can be called anywhere in a program, but rather it must be called on an instance of the class from which it was derived. A method takes <i>self</i> as an argument, <i>self</i> being the instance of the class that the method is being called on. For an instance to call a method, the method must be defined either in the class from which the instance was derived, or in one of that class's parent classes.

5. What is an instance in object orientation?

    An instance is an occurance of a class. It can reference any of its parent class's methods and attributes.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute belongs to a class, whereas an instance attribute lives on each object instantiated from a class. 

   That means that if you decide to instantiate a class with a particular instance attribute (or even add the instance attribute after instantiation), each instance will have a unique place in memory for its instance attribute. A thousand instances means a thousand instance attributes (assuming you initiate the object with the attribute).

    With a class attribute, the attribute lives with the class, so all instances of the class will have access to the attribute, but the attribute will only live in one place in memory, with the class.

    If you expect all or most of the instances of a class to have the same attribute, like all the members of a dog class having the species 'dog,' you'd want to use a class attribute. That way you don't have many places in memory storing the same information.

    If you expect the instances to need unique attributes, like a person's name or a credit card number, an instance attribute would make more sense.


"""


# Part 2: classes and init methods

class Student(object):
    """A student class, takes a first name, last name, and address as arguments.
    """
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question class, takes a question and a correct answer as arguments.
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """asks user the question, returns true or false based on answer
        """
        answer = raw_input(self.question + " > ")
        if answer == self.answer:
            return True
        return False


class Exam(object):
    """An exam class, takes an exam name as an argument.
    """
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        """Adds a question and answer to the exam
        """
        self.questions.append(Question(question, answer))

    def administer(self):
        """Administers all exam questions, returns score at end.
        """
        score = 0.0
        for question in self.questions:
            add_point = question.ask_and_evaluate()
            if add_point:
                score += 1.0
        return score


# Part 3: methods
# Part 4: Create and exam
def take_test(exam, student):
    """Takes an exam and a student as parameters, administers exam, assigns student score.
    """
    student.score = exam.administer()

def example():
    """Creates an exam and a student, administers text for student.
    """
    exam = Exam('example exam')
    exam.add_question('what is your name?', 'sir lancelot of camelot')
    exam.add_question('what is your quest?', 'to seek the holy grail')
    exam.add_question('what is your favorite color?', 'blue')
    exam.add_question('what is the capital of Assyria?', 'Nineveh')
    exam.add_question('what is the airspeed velocity of an unladen swallow?', 'an African or European swallow?')
    student = Student('Sir Lancelot', "of Camelot", "12307 Camel Lot Lane")
    take_test(exam, student)
    return exam, student

# Part 5: Inheritance
class Quiz(Exam):
    """subclass of Exam, returns true if you answer at least half the questions correctly.
    """
    def administer(self):
        """Administers quiz"""
        score = super(Quiz, self).administer()
        if score >= len(self.questions) /  2.0:
            return True
        return False





