# **University Progression Outcomes Predictor**

## Overview

This program predicts academic progression outcomes for university students based on their credit distribution at the end of each academic year. It is divided into multiple parts to accommodate different user requirements, from individual student predictions to staff-level bulk processing and visualization.

## Features

### Part 1: Student Version
- Allows students to predict their progression outcome.
- Prompts for the number of credits at pass, defer, and fail.
- Displays the appropriate progression outcome (e.g., progress, module trailer, module retriever, exclude).

### Part 2: Validation
- Extends Part 1 to add input validation.
- Ensures credit inputs are integers and within the acceptable range (0, 20, 40, 60, 80, 100, 120).
- Checks that the total of pass, defer, and fail credits is 120.
- Loops until acceptable inputs are entered.

### Part 3: Staff Version with Histogram
- Allows staff to input credits for multiple students.
- Displays a histogram of progression outcomes upon completion.
- Provides a count of students in each progression category.

### Part 4: Vertical Histogram (Optional)
- Extends Part 3 to include a vertical histogram for visualizing progression outcomes.

### Part 5: Alternative Staff Version (Optional)
- Uses predefined data from a list, tuple, or dictionary instead of user input.
- Displays a histogram based on this data.
