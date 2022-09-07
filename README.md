# Rocketry-Bot
 A discord bot for administrative and notification purposes.

# Features
Features can be disabled individually
## Member Database
Creates and manages names and automatically assigns the aspiring member role once they have submitted their name and rose-hulman email address.

## Attendance Taking
*Requires Member Database*

Based on the Google Calendar (updated hourly) provided, it will create a message in channel to react to.
This will automatically mark down the hours worked log for an hour (default) or special by an admin.

This also manages the `Active` or `Aspiring` member status. If the member has not submitted attendance for a quarter they will be demoted to `Aspiring` member. This rule does not apply to admin.

## Launch Day Alerts
When a launch day is coming up or arrived, a generated report for drive time, weather, and other information will be sent in announcements. 

## USLI Project Alerts
Reminds us of upcoming due dates for USLI reports.