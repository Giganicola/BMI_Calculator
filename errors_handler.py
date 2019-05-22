"""
BMI App

Author: Nicola Simioni
Email:  info@nicolasimioni.com
"""


# This class handles error messages
class ErrorsHandler:

    # Highlight weight errors
    def highlight_weight_errors(self):
        self.errors.config(text='Please insert positive values')
        self.error_messages_frame.config(background='#ffb3b3')
        self.errors.config(background='#ffb3b3')
        self.w_stones.config(background='#ffb3b3')
        self.w_pounds.config(background='#ffb3b3')
        self.w_kgs.config(background='#ffb3b3')

    # Highlight height errors
    def highlight_height_errors(self):
        self.errors.config(text='Please insert positive values')
        self.error_messages_frame.config(background='#ffb3b3')
        self.errors.config(background='#ffb3b3')
        self.h_cms.config(background='#ffb3b3')
        self.h_feet.config(background='#ffb3b3')
        self.h_inches.config(background='#ffb3b3')

    # Reset weight error warnings
    def reset_weight_errors(self):
        self.w_kgs.config(background='#FFFFFF')
        self.w_stones.config(background='#FFFFFF')
        self.w_pounds.config(background='#FFFFFF')
        self.errors.config(text='')
        self.error_messages_frame.config(background='#CCCCCC')
        self.errors.config(background='#CCCCCC')
        self.user_name.config(background='#FFFFFF')
        self.bmi_result.config(text='')
        self.bmi_message.config(text='')

    # Reset height error warnings
    def reset_height_errors(self):
        self.h_cms.config(background='#FFFFFF')
        self.h_feet.config(background='#FFFFFF')
        self.h_inches.config(background='#FFFFFF')
        self.errors.config(text='')
        self.error_messages_frame.config(background='#CCCCCC')
        self.errors.config(background='#CCCCCC')
        self.user_name.config(background='#FFFFFF')
        self.bmi_result.config(text='')
        self.bmi_message.config(text='')

    # Reset height error warnings
    def reset_username(self):
        self.user_name.config(background='#FFFFFF')
        self.errors.config(text='')
        self.error_messages_frame.config(background='#CCCCCC')
        self.errors.config(background='#CCCCCC')

    # Highlight non int value errors
    def invalid_input(self):
        self.errors.config(text='Please insert integer values')
        self.error_messages_frame.config(background='#ffb3b3')
        self.errors.config(background='#ffb3b3')
