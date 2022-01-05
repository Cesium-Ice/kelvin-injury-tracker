# kelvin-injury-tracker

This is code to power a tumblr blog keeping track of the days since [Kelvin](
https://twitter.com/NotCelsiusDeg) last injured himself. 

Link to blog: https://kelvin-injury-tracker.tumblr.com/

---

The script update_tracker.py is run by an AWS lambda function and triggers once per day via Cloudwatch

To create reports of new injuries run ```python report_injury.py injury_area injury_cause```  

---

If for some unfathonable reason you want to create your own tumblr blog keeping track of this (or something equally frivolous), use the [tumblr api](https://www.tumblr.com/docs/en/api/v2) to register an application and get your own auth tokens.

