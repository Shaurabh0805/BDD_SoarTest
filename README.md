Install the following: <br>
pip install pytest-behave<br>
pytest --behave<br>
pip install behave-html-formatter<br>
<br>
To run the Behave tests:<br>
behave -f html -o bdd_load_test_report.html<br>

To run stress tests on Client_login<br>
locust -f locustfile_client_login.py --headless --users 50 --spawn-rate 5 --run-time 5m --html stress_test_report.html<br>

To run load tests on Client_register<br>
locust -f locustfile_client_register.py --headless --users 10 --spawn-rate 10 --run-time 2m --html load_test_report.html<br>
