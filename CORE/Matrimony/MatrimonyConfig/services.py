from CORE.utils import getCommonResponse

def landing_page_data():
    context = {
        'success_stories' : [
            [{'img': "static/website/images/wp01.png", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}],
            [{'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}],
            [{'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}, {'img': "asdfdas", 'couple': "mr. & mrs."}],
        ],
        'faqs': [
            {
                'id': 0,
                'quens': "What does Bibahoovijan do?",
                'ans': "Bibahoovijan is an online platform designed to help individuals find their life partners. We have provided a platform for people to create profiles, search for potential matches based on their criteria, and communicate with each other.",
            },
            {
                'id': 1,
                'quens': "Is the site secure ?",
                'ans': "Yes, We take security and privacy seriously. We have implemented measures such as encryption, secure connections, and verification processes to ensure the safety of user data. However, it is always important to be cautious and avoid sharing sensitive information with unknown individuals outside of our platform."
            },
            {
                'id': 2,
                'quens': "How can I register to the platform?",
                'ans': "Our registration procedure is simple and straight forward. All you need is a valid mobile number and email address."
            },
            {
                'id': 3,
                'quens': "What kind of information is required to create a profile?",
                'ans': "When creating a profile on a this site, you will typically be asked to provide details such as name, age, gender, religion, educational background, occupation, family background, and partner preferences."
            },
            {
                'id': 4,
                'quens': "Can I search for matches based on specific criteria?",
                'ans': "Yes, We offer advanced search options that allow you to customize your search based on various criteria such as age, location, religion, educational qualifications, occupation, and more. This helps you narrow down the options to find potential matches that meet your preferences."
            },
            {
                'id': 5,
                'quens': "Are the profiles on Bibahoovijan verified?",
                'ans': "We have a verification process in place to ensure the authenticity of profiles. We verify phone numbers, email addresses, or request documents to confirm the identity and background information of users. However, it's still essential to exercise caution and use your judgment while interacting with others online."
            },
            {
                'id': 6,
                'quens': "Is there a fee for using this site?",
                'ans': "Currently registration, profile creation and searching is completely free."
            },
            {
                'id': 7,
                'quens': "Can I delete my account or posts if I no longer want to use this site?",
                'ans': "You can delete your posts and account any time you want. But we encourage you to deactivate your profile so that you can return and continue using our platform any time without any hassle."
            },
            {
                'id':8,
                'quens': "Can I report or block users who behave inappropriately?",
                'ans': "Yes, We provide options to report or block users who engage in inappropriate behavior.If you come across someone who violates the site's terms of service or makes you uncomfortable, you can use the reporting or blocking feature to protect yourself and notify the site administrators."
            },
        ],
    }
    return context

