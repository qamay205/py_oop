"""
Description: Create TestRail client for generating Test Suites

Features:
- TestSuite should be created with (username list(First Name/Last Name), user_email, user_password)
- Show in test cases all user data except password (password should be shown as '********')
- Create test suite for login/registration/article create flow
- Please use the same steps in common methods
- Validate valid user email and profile

Testing:
- Run all your testsuite using calling methods for suite_object
"""


class TestRunBuilder:
    url = 'https://react-redux.realworld.io/'
    sign_in_url = 'https://react-redux.realworld.io/#/login?_k=yk65kp'
    sign_up_url = 'https://react-redux.realworld.io/#/register?_k=p3y1e3'
    article_page_url = 'https://react-redux.realworld.io/#/editor?_k=rl7ioi'
    article_input_data = 'Frendship'

    def __init__(self, first_name, last_name, user_email, user_password):
        print("Launched")
        self.full_name = first_name + last_name
        if '@' and '.' in user_email:
            self.email = user_email
        else:
            print('Check entered email, @ symbol is missing')
        if len(user_password)>= 8:
            self.password = user_password
        else:
            print('The entered password is less than 8 symbols, please change it')

    def login_flow(self):
        print(f'1. open the {self.sign_in_url} website')
        print(f'2. enter {self.email} into the email field')
        print(f'3. enter {self.password} into the password field')
        print(f'4. click the [Sign in] button')

    def hello(self):
        print(f'Hello {self.full_name}, you are in {self.url}')

    def registration_suite(self):
        print('registration______________________________________')
        print(f'1. open the {self.sign_up_url} website')
        print(f'2. enter {self.full_name} into the username field')
        print(f'3. enter {self.email} into the email field')
        print(f'4. enter {self.password} into the password field')
        print(f'5. click the [Sign up] button')

    def login_suite(self):
        print('login__________________________________________')
        self.login_flow()

    def article_create_suite(self):
        print('article_create____________________________________')
        self.login_flow()
        print(f'5. open the {self.article_page_url} page')
        print(f'6. enter {self.article_input_data} into the article_title field')
        print(f'7. enter {self.article_input_data} into the article_about field')
        print(f'8. enter {self.article_input_data} into the article_content field')
        print(f'9. click the [Publish article] button')

    def smoke_test_run(self):
        self.login_suite()

    def sanity_test_run(self):
        self.registration_suite()

    def regression_test_run(self):
        self.login_suite()
        self.registration_suite()
        self.article_create_suite()

conduit_test_run = TestRunBuilder('Pinky ', 'Pie', 'equestria@gmail.com', 'partyParty')
conduit_test_run.hello()
conduit_test_run.login_suite()
conduit_test_run.registration_suite()
conduit_test_run.article_create_suite()

