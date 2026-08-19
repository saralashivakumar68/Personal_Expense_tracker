# Personal_Expense_tracker
Personal_Expense_tracker
# 💰 Personal Expense Tracker

A beginner-friendly **command-line Personal Expense Tracker built with Python**.

This project was created to practice core Python concepts by building a practical application that allows users to record expenses, view spending details, calculate total spending, find the highest and lowest expenses, search expenses, and generate a category-wise spending summary.

## 🚀 Features

- ➕ Add new expenses
- 📋 View all recorded expenses
- 💰 Calculate total spending
- 📈 Find the highest expense
- 📉 Find the lowest expense
- 🔎 Search expenses
- 📊 Generate category-wise expense summary
- 🔄 Interactive menu-driven system
- 🚪 Exit the application

## 🧾 Expense Information

Each expense contains three pieces of information:

```python
{
    "Amount": 250,
    "Category": "Food",
    "Description": "Lunch"
}
Expenses = [
    {
        "Amount": 250,
        "Category": "Food",
        "Description": "Lunch"
    },
    {
        "Amount": 100,
        "Category": "Travel",
        "Description": "Bus"
    }
]
================================================
             PERSONAL EXPENSE TRACKER
================================================

Option 1 → Add Expenses
Option 2 → View All Expenses
Option 3 → Total Expenses
Option 4 → Highest Expenses
Option 5 → Search Items
Option 6 → Category Summary
Option 7 → Exit
Example Category Summary
If the recorded expenses are:
Food       → ₹250
Travel     → ₹100
Food       → ₹150
Education  → ₹500
The category summary becomes:
========== CATEGORY SUMMARY ==========

Food      : ₹400
Travel    : ₹100
Education : ₹500


