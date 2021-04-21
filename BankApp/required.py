# Banking Application API

## Description

# The Banking App API is a Server - side application that facilitates the management of
# Client's Bank Accounts. A client create new accounts of various categories. Clients
# can deposit or withdraw funds from the account as well as close out accounts.
#
# ## Purpose
# We want to see that you can meet deadlines and that you can code. You are expected to complete the following
# requirements and give a 5 minute presentation of your project to our QC team.

## Requirements
# 1. All endpoints listed below must have a Postman test verifying functionality
# 2. Data is stored in a database.
# 3. Data Access is performed through the use of Data Access Objects.
# 5. All input is sent from a client (Postman) and handled by the Server
# 6. Logging is implemented throughout the application
# 7. All DAO and Service methods must have a test proving that they work

## RESTful Endpoints:

# POST /clients => Creates a new client
# 	return a 201 status code

# -- send new client "name="", account="1"(by default), account_value="100"
# -- alert 201 status

# GET /clients => gets all clients
# 	return 200
# -- index list of clients
# -- alert 200
#
# GET /clients/10 => get client with id of 10
# 	return 404 if no such client exist

# -- get client by id
# -- if id == false or client.id == inactive: alert 404 client not found
#
# PUT /clients/12 => updates client with id of 12
# 	return 404 if no such client exist

# -- update client.id info
# -- if client.id alert 404 or if client.id == inactive alert inactive
#
# DELETE /clients/15 => deletes client with the id of15
# 	return 404 if no such client exist
# 	return 205 if success

# -- set client.id to inactive
# -- if no client.id alert 404
#  -- if client.id inactive alert account inactive(case shouldnt exist)
#  -- if success alert 205
#
#
# POST /clients/5/accounts =>creates a new account for client with the id of 5
# 	return a 201 status code

# -- post new account with initial value of 0 or input amount
# -- alert 201
#
# GET /clients/7/accounts => get all accounts for client 7
# 	return 404 if no client exists

# -- index list of client.id accounts
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive
#
# GET /clients/7/accounts?amountLessThan=2000&amountGreaterThan400 => get all accounts
# for client 7 between 400 and 2000
# 	return 404 if no client exists

# -- index list of client.id account where value is > 500 and < 2000
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive
#
# GET /clients/9/accounts/4 => get account 4 for client 9
# 	return 404 if no account or client exists

# -- get client.id.account.id
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive
#
# PUT /clients/10/accounts/3 => update account  with the id 3 for client 10
# 	return 404 if no account or client exists

# -- update client.id.account.id
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive
#
# DELETE /clients/15/accounts/6 => delete account 6 for client 15
# 	return 404 if no account or client exists

# -- delete client.id.account.id if value is 0 if value is not 0 alert "should empty account before deleting"
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive
#
#
# PATCH /clients/17/accounts/12 => Withdraw/deposit given amount (Body: {"deposit":500} or {"withdraw":250}
# 	return 404 if no account or client exists
# 	return 422 if insufficient funds

# -- update client.id.account.id
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive
#
# PATCH /clients/12/accounts/7/transfer/8 => transfer funds from account 7 to account 8 (Body: {"amount":500})
# 	return 404 if no client or either account exists
# 	return 422 if insufficient funds

# -- get client.id.account.id update value if withdraw amount > account.value alert "insufficient funds"
# -- get client.id.account.id update value
# -- if no client.id alert 404
#  -- if client.id is inactive alert inactive