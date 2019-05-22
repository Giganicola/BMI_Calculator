"""
BMI App

Author: Nicola Simioni
Email:  info@nicolasimioni.com
"""

from tkinter import *
import math
from errors_handler import ErrorsHandler


class Converter:

    # Converts weight units
    def weight_conversion(self, unit):
        if unit in {'kgs'}:

            # Reset error message and entries
            ErrorsHandler.reset_weight_errors(self)

            # Check for non int values
            try:
                kgs = int(self.w_kgs.get())

                # Check for negative value
                if kgs < 0:
                    ErrorsHandler.highlight_weight_errors(self)

                # Conversion
                kg_to_stones = kgs / 6.35029318
                result = math.modf(kg_to_stones)

                stones = result[1]
                pounds = result[0] * 14

                self.w_stones.delete(0, END)
                self.w_stones.insert(0, round(stones))
                self.w_pounds.delete(0, END)
                self.w_pounds.insert(0, round(pounds))
                self.bmi_kgs = round(kgs)

            except ValueError:
                ErrorsHandler.invalid_input(self)
                self.errors.config(background='#ffb3b3')
                self.w_kgs.config(background='#ffb3b3')

        if unit in {'stones', 'pounds'}:

            # Reset error message and entries
            ErrorsHandler.reset_weight_errors(self)

            # Check for non int values
            try:
                stones = int(self.w_stones.get())
                pounds = int(self.w_pounds.get())

                # Check for negative value
                if stones < 0:
                    ErrorsHandler.highlight_weight_errors(self)

                if pounds < 0:
                    ErrorsHandler.highlight_weight_errors(self)

                # Conversion
                stone_to_kg = stones * 6.35029318
                pounds_to_kg = pounds * 0.45359237

                kgs = stone_to_kg + pounds_to_kg

                self.w_stones.delete(0, END)
                self.w_stones.insert(0, round(stones))
                self.w_pounds.delete(0, END)
                self.w_pounds.insert(0, round(pounds))
                self.w_kgs.delete(0, END)
                self.w_kgs.insert(0, round(kgs))
                self.bmi_kgs = round(kgs)

            except ValueError:
                ErrorsHandler.invalid_input(self)
                self.errors.config(background='#ffb3b3')
                self.w_stones.config(background='#ffb3b3')
                self.w_pounds.config(background='#ffb3b3')


    # Converts height units
    def height_conversion(self, unit):
        if unit in {'cms'}:

            # Reset error message and entries
            ErrorsHandler.reset_height_errors(self)

            # Check for non int values
            try:
                cms = int(self.h_cms.get())

                # Check for negative value
                if cms < 0:
                    ErrorsHandler.highlight_height_errors(self)

                # Conversion
                cm_to_feet = cms * 0.0328084
                result = math.modf(cm_to_feet)

                feet = result[1]
                inches = result[0] * 12

                self.h_feet.delete(0, END)
                self.h_feet.insert(0, round(feet))

                self.h_inches.delete(0, END)
                self.h_inches.insert(0, round(inches))

                self.bmi_cms = round(cms)

            except ValueError:
                ErrorsHandler.invalid_input(self)
                self.errors.config(background='#ffb3b3')
                self.h_cms.config(background='#ffb3b3')

        if unit in {'feet', 'inches'}:

            # Reset error message and entries
            ErrorsHandler.reset_height_errors(self)

            # Check for non int values
            try:
                feet = int(self.h_feet.get())
                inches = int(self.h_inches.get())

                # Check for negative value
                if feet < 0:
                    ErrorsHandler.highlight_height_errors(self)

                if inches < 0:
                    ErrorsHandler.highlight_height_errors(self)

                # Conversion
                feet_to_cm = feet / 0.0328084
                inches_to_cm = inches / 0.39370

                cms = feet_to_cm + inches_to_cm

                self.h_feet.delete(0, END)
                self.h_feet.insert(0, round(feet))

                self.h_inches.delete(0, END)
                self.h_inches.insert(0, round(inches))

                self.h_cms.delete(0, END)
                self.h_cms.insert(0, round(cms))

                self.bmi_cms = round(cms)

            except ValueError:
                ErrorsHandler.invalid_input(self)
                self.h_feet.config(background='#ffb3b3')
                self.h_inches.config(background='#ffb3b3')
