
!---------eRwin Automation Scripts.-------------------------------!!!!

!---------Author: Shikha Singh (Shikha.Singh@sqs.com)-----------------!!!!!





This folder contains Python script to automate erWin Application.

Currently it has two scripts:



1. erWin login-logout - it is simple login-logout script & perform following steps:

	a. open erWin-Audi application

	b. login with user1

	c. logout



2. 69979 - ERW_083_002 Display ElsaPro with VIN- it is a test case which displays Elsapro for a specific VIN. It performs following steps:

	a. open erWin-Audi application

	b. login with user1

	c. open Vehicle Identification Page

	d. Enter VIN

	e. Click "Search"

	f. Click "Repair and Maintenance"

	f. Open ElsaPro

	g. Logout



After the execution of the script, test report is generated in HTML format.

To generate Script, following are the pre requisites:

a."HTMLTestRunner.py" & "test_HTMLTestRunner.py" should be present in the same directory as the script.

b. Run "test_HTMLTestRunner.py" and you should see "erWinTestReport.html" file generated in the same directory



After execution, email containing the status (Pass/Fail) of the test case is sent automatically to "alexasqs123@gmail.com".



This Reoprt can also be seen by opening "erWinTestReport.html".

