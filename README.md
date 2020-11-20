# API_integration
## Some feedbacks regarding the API
1. > 200 character validation for description is flawed
2. should use unix ts for date, field should use int64 instead of string, better to use unix ts, as clients might report date based on local tz
3. e-mail validation is not complete, it accepts "asd.com@nodomain", right now its only checking if "@" exists.
