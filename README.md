# exposure-notification-server

## Test data
Run the following script `./test_data.sh`

## Starting the server 

### On Windows
`./start_server.sh`

### On bash
First activate the pip package manager by running the activate script, `source venv/bin/activate`.
Afterwards, run `./start_server.sh`

## API calls

### POST: /update-status
Updates the status of a token.

### POST: /delete-token
Deletes a token.

### GET: /get-tokens
Returns all of tokens stored in the database.

### GET: /get-student-tokens
Returns all of tokens generated by a given student.

### GET: /get-exposure-list
Returns a list of all tokens that may have been exposed to covid-19.

### GET: /get-monthly-checkins
Returns a list of monthly check ins with a count of exposed and non-exposed tokens. 

### POST: /submit-token
Submits an encrypted token to the database, this token will be decrypted before being added to the database.
