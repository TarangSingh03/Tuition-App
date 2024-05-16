from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from copy import deepcopy



class LocationSelectionPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.states = [
            'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
            'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
            'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
            'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
            'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
        ]
        self.dropdown = DropDown()
        for state in self.states:
            btn = Button(text=state, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text='Select State', size_hint=(None, None))
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.mainbutton.bind(on_press=self.on_next)

        self.add_widget(self.mainbutton)

    def on_next(self, instance):
        selected_state = self.mainbutton.text
        if selected_state != 'Select State':
            self.manager.selected_state = selected_state
            self.manager.current = 'city_selection'
        else:
            pass


class CitySelectionPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = DropDown()
        self.cities = []

    def on_pre_enter(self):
        selected_state = self.manager.selected_state
        self.cities = self.get_cities(selected_state)

        for city in self.cities:
            btn = Button(text=city, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text='Select City', size_hint=(None, None))
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.mainbutton.bind(on_press=self.on_next)

        self.add_widget(self.mainbutton)

    def on_next(self, instance):
        selected_city = self.mainbutton.text
        if selected_city != 'Select City':
            self.manager.selected_city = selected_city
            self.manager.current = 'class_selection'
        else:
            pass

    def get_cities(self, state):
        # Simulated data, replace with actual logic to fetch cities for the selected state
        if state == 'Andhra Pradesh':
            return ['Vijayawada', 'Visakhapatnam', 'Guntur']
        elif state == 'Arunachal Pradesh':
            return ['Itanagar', 'Naharlagun']
        elif state == 'Assam':
            return ['Guwahati', 'Dibrugarh', 'Silchar']
        elif state == 'Bihar':
            return ['Patna', 'Gaya', 'Bhagalpur']
        elif state == 'Chhattisgarh':
            return ['Raipur', 'Bhilai', 'Bilaspur']
        elif state == 'Goa':
            return ['Panaji', 'Margao', 'Vasco Da Gama']
        elif state == 'Gujarat':
            return ['Ahmedabad', 'Surat', 'Vadodara']
        elif state == 'Haryana':
            return ['Faridabad', 'Gurgaon', 'Panipat']
        elif state == 'Himachal Pradesh':
            return ['Shimla', 'Mandi', 'Dharamshala']
        elif state == 'Jharkhand':
            return ['Ranchi', 'Jamshedpur', 'Dhanbad']
        elif state == 'Karnataka':
            return ['Bangalore', 'Mysore', 'Hubli']
        elif state == 'Kerala':
            return ['Kochi', 'Thiruvananthapuram', 'Kozhikode']
        elif state == 'Madhya Pradesh':
            return ['Indore', 'Bhopal', 'Jabalpur']
        elif state == 'Maharashtra':
            return ['Mumbai', 'Pune', 'Nagpur']
        elif state == 'Manipur':
            return ['Imphal', 'Thoubal', 'Kakching']
        elif state == 'Meghalaya':
            return ['Shillong', 'Tura', 'Jowai']
        elif state == 'Mizoram':
            return ['Aizawl', 'Lunglei', 'Saiha']
        elif state == 'Nagaland':
            return ['Kohima', 'Dimapur', 'Mokokchung']
        elif state == 'Odisha':
            return ['Bhubaneswar', 'Cuttack', 'Rourkela']
        elif state == 'Punjab':
            return ['Ludhiana', 'Amritsar', 'Jalandhar']
        elif state == 'Punjab':
            return ['Ludhiana', 'Amritsar', 'Jalandhar']
        elif state == 'Sikkim':
            return ['Gangtok', 'Namchi', 'Mangan']
        elif state == 'Rajasthan':
            return ['Jaipur', 'Udaipur', 'Jodhpur']
        elif state == 'Tamil Nadu':
            return ['Chennai', 'Coimbatore', 'Madurai']
        elif state == 'Telangana':
            return ['Hyderabad', 'Warangal', 'Nizamabad']
        elif state == 'Tripura':
            return ['Agartala', 'Udaipur', 'Dharmanagar']
        elif state == 'Uttar Pradesh':
            return ['Lucknow', 'Kanpur', 'Varanasi', 'Agra']
        elif state == 'Uttarakhand':
            return ['Dehradun', 'Haridwar', 'Roorkee']
        elif state == 'West Bengal':
            return ['Kolkata', 'Howrah', 'Durgapur']
        # Add more states and cities here


class ClassSelectionPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.classes = ['Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8',
                        'Class 9', 'Class 10', 'Class 11', 'Class 12', 'Graduation']

        self.dropdown = DropDown()
        for class_level in self.classes:
            btn = Button(text=class_level, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text='Select Class', size_hint=(None, None))
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.mainbutton.bind(on_press=self.on_next)

        self.add_widget(self.mainbutton)

    def on_next(self, instance):
        selected_class = self.mainbutton.text
        if selected_class != 'Select Class':
            self.manager.selected_class = selected_class
            self.manager.current = 'course_selection'
        else:
            pass


class CourseSelectionPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.courses = ['Web Development', 'Mathematics', 'Science', 'Art', 'Drawing', 'Chemistry', 
                        'Physics', 'English', 'Hindi', 'Quantum Computing', 'Engineering Mathematics', 
                        'Programming Languages']

        self.dropdown = DropDown()
        for course in self.courses:
            btn = Button(text=course, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text='Select Course', size_hint=(None, None))
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.mainbutton.bind(on_press=self.on_next)

        self.add_widget(self.mainbutton)

    def on_next(self, instance):
        selected_course = self.mainbutton.text
        if selected_course != 'Select Course':
            self.manager.selected_course = selected_course
            self.manager.current = 'course_details'
        else:
            pass


class CourseDetailsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tuition_centers = {
            'Hindi': [
                {'name': 'EduCare', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'},
                {'name': 'KidGenius', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'}
            ],
            'English': [
                {'name': 'KidGenius', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'},
                {'name': 'EduCare', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'}
            ],
            'Art': [
                {'name': 'ExcelAcademy', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'BrilliantMinds', 'duration': '5 months', 'start_date': 'June 15, 2024', 
                 'fee': 'Rs. 12,000', 'address': '555 Pine Street, City', 'teacher': 'Sophia Patel'},
                {'name': 'GeniusHub', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 18,000', 'address': '666 Birch Street, City', 'teacher': 'Oliver Kim'},
                {'name': 'KidGenius', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'}
            ],
            'Web Development': [
                {'name': 'EduCare', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'},
                {'name': 'Mastermind Tutoring Services', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'}
            ],
            'Mathematics': [
                {'name': 'Success Point Education', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'},
                {'name': 'Mastermind Tutoring Services', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'}
            ],
            'Science': [
                {'name': 'ExcelAcademy', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'Elite Learning Center', 'duration': '5 months', 'start_date': 'June 15, 2024', 
                 'fee': 'Rs. 12,000', 'address': '555 Pine Street, City', 'teacher': 'Sophia Patel'},
                {'name': 'GeniusHub', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 18,000', 'address': '666 Birch Street, City', 'teacher': 'Oliver Kim'},
                {'name': 'Mastermind Tutoring Services', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'}
            ],
            'Drawing': [
                {'name': 'EduCare', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'},
                {'name': 'KidGenius', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'}
            ],
            'Chemistry': [
                {'name': 'Smart Scholars Institute', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'},
                {'name': 'Mastermind Tutoring Services', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'}
            ],
            'Physics': [
                {'name': 'Academic Excellence Hub', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'BrilliantMinds', 'duration': '5 months', 'start_date': 'June 15, 2024', 
                 'fee': 'Rs. 12,000', 'address': '555 Pine Street, City', 'teacher': 'Sophia Patel'},
                {'name': 'GeniusHub', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 18,000', 'address': '666 Birch Street, City', 'teacher': 'Oliver Kim'},
                {'name': 'ExcelAcademy', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'Knowledge Quest Institute', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 20,000', 'address': '659 Birch Street, City', 'teacher': 'Oliver Kim'}
            ],
            'Quantum Computing': [
                {'name': 'Mastermind Tutoring Services', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'},
                {'name': 'ExcelAcademy', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'BrilliantMinds', 'duration': '5 months', 'start_date': 'June 15, 2024', 
                 'fee': 'Rs. 12,000', 'address': '555 Pine Street, City', 'teacher': 'Sophia Patel'},
                {'name': 'Knowledge Quest Institute', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 18,000', 'address': '666 Birch Street, City', 'teacher': 'Oliver Kim'}
            ],
            'Engineering Mathematics': [
                {'name': 'Future Leaders Academy', 'duration': '6 months', 'start_date': 'April 20, 2024', 
                 'fee': 'Rs. 12,000', 'address': '111 Main Street, City', 'teacher': 'Alice Johnson'},
                {'name': 'SmartStart', 'duration': '5 months', 'start_date': 'June 10, 2024', 
                 'fee': 'Rs. 10,000', 'address': '222 Elm Street, City', 'teacher': 'David Lee'},
                {'name': 'BrightSparks', 'duration': '7 months', 'start_date': 'May 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '333 Oak Street, City', 'teacher': 'Emily Chen'},
                {'name': 'ExcelAcademy', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'BrilliantMinds', 'duration': '5 months', 'start_date': 'June 15, 2024', 
                 'fee': 'Rs. 12,000', 'address': '555 Pine Street, City', 'teacher': 'Sophia Patel'},
                {'name': 'Knowledge Quest Institute', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 18,000', 'address': '666 Birch Street, City', 'teacher': 'Oliver Kim'}
            ],
            'Programming Languages': [
                {'name': 'ExcelAcademy', 'duration': '6 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 15,000', 'address': '444 Maple Street, City', 'teacher': 'Michael Wang'},
                {'name': 'BrilliantMinds', 'duration': '5 months', 'start_date': 'June 15, 2024', 
                 'fee': 'Rs. 12,000', 'address': '555 Pine Street, City', 'teacher': 'Sophia Patel'},
                {'name': 'Knowledge Quest Institute', 'duration': '7 months', 'start_date': 'May 5, 2024', 
                 'fee': 'Rs. 18,000', 'address': '666 Birch Street, City', 'teacher': 'Oliver Kim'},
                {'name': 'Mastermind Tutoring Services', 'duration': '6 months', 'start_date': 'June 1, 2024', 
                 'fee': 'Rs. 10,000', 'address': '123 ABC Street, City', 'teacher': 'John Doe'},
                {'name': 'LearnSmart', 'duration': '5 months', 'start_date': 'May 15, 2024', 
                 'fee': 'Rs. 8,000', 'address': '456 XYZ Avenue, City', 'teacher': 'Jane Smith'},
                {'name': 'BrightMinds', 'duration': '7 months', 'start_date': 'July 1, 2024', 
                 'fee': 'Rs. 12,000', 'address': '789 PQR Road, City', 'teacher': 'Tom Brown'}
            ],
            # Add data for other courses
        }

        self.course_label = Label(text='')
        self.center_dropdown = DropDown()

        self.add_widget(self.course_label)

    def on_pre_enter(self):
        selected_course = self.manager.selected_course

        self.course_label.text = f'Available Centers for {selected_course}:'

        centers = self.tuition_centers.get(selected_course, [])
        for center in centers:
            btn = Button(text=center['name'], size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn, center_info=deepcopy(center): self.on_select_center(center_info))
            self.center_dropdown.add_widget(btn)

        self.mainbutton = Button(text='Select Center', size_hint=(None, None))
        self.mainbutton.bind(on_release=self.center_dropdown.open)
        self.center_dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        self.add_widget(self.mainbutton)

    def on_select_center(self, center_info):
        self.manager.selected_center_info = center_info
        self.manager.current = 'center_details'

class CenterDetailsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.center_details_label = Label(text='')

        self.add_widget(self.center_details_label)

    def on_pre_enter(self):
        selected_center_info = self.manager.selected_center_info

        details = f'Name: {selected_center_info["name"]}\n' \
                  f'Fee: {selected_center_info["fee"]}\n' \
                  f'Duration: {selected_center_info["duration"]}\n' \
                  f'Address: {selected_center_info["address"]}\n' \
                  f'Start Date: {selected_center_info["start_date"]}\n' \
                  f'Teacher: {selected_center_info["teacher"]}'

        self.center_details_label.text = details

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.selected_state = ''

        sm.add_widget(LocationSelectionPage(name='location_selection'))
        sm.add_widget(CitySelectionPage(name='city_selection'))
        sm.add_widget(ClassSelectionPage(name='class_selection'))
        sm.add_widget(CourseSelectionPage(name='course_selection'))
        sm.add_widget(CourseDetailsPage(name='course_details'))
        sm.add_widget(CenterDetailsPage(name='center_details'))

        return sm


if __name__ == '__main__':
    MyApp().run()
