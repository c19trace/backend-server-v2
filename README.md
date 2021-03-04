# exposure-notification-server

## Starting the server
`./start_server.sh`

## setup log synchronization
Syncs logs every 4 hours
`echo "* */4 * * * sh /app/sync.sh 2>/dev/null" >> /etc/crontab`

## Api calls
### GET: /get-exposure-list
Returns a list of all random id's that may have been exposed to covid-19.

### POST: /submit-exposure-list
#### params: key (api key), randomids (comma seperated list of randomids)
Allows backend server to publish new exposed random ids.

