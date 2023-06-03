Please Find Below The Curl Requests:


1# first create-super user and authenticated using JWT

    
    curl --location 'http://127.0.0.1:8000/api/token/' \
    --header 'Content-Type: application/json' \
    --data '{
        "username":"rahul",
        "password":"rahul"
        
    
    }'

2# Created the Alert :
    
    curl --location 'http://127.0.0.1:8000/alerts/create/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Nzk2OTQ0LCJpYXQiOjE2ODU3OTYwNDQsImp0aSI6ImVhNGFmOWM5Y2M2ZjQ2Njc4ZTU1ZGIxYjIyNTkyM2FkIiwidXNlcl9pZCI6MX0.f2W_LbMYvSdRsz7lYU-01ubscmNzJHrSjwtlxFppLxI' \
    --data '{
        "target_price":27168,
        "currency_id":1
    }'

3# did filter here:
    status = created or deleted or triggered
    scope of caching is less as it is paginated response , but if nothing changes then DB does the caching
    
    curl --location 'http://127.0.0.1:8000/alerts/fetch/?limit=20&offset=0&status=created' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Nzk2OTQ0LCJpYXQiOjE2ODU3OTYwNDQsImp0aSI6ImVhNGFmOWM5Y2M2ZjQ2Njc4ZTU1ZGIxYjIyNTkyM2FkIiwidXNlcl9pZCI6MX0.f2W_LbMYvSdRsz7lYU-01ubscmNzJHrSjwtlxFppLxI'

4# delete the Alert:
    
    curl --location --request DELETE 'http://127.0.0.1:8000/alerts/delete/2/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Nzk2OTQ0LCJpYXQiOjE2ODU3OTYwNDQsImp0aSI6ImVhNGFmOWM5Y2M2ZjQ2Njc4ZTU1ZGIxYjIyNTkyM2FkIiwidXNlcl9pZCI6MX0.f2W_LbMYvSdRsz7lYU-01ubscmNzJHrSjwtlxFppLxI'


5# one task is running periodic so if any price is matched then it checks instead of DB if CACHE is present as it is much faster

6# I used BTC only but we can add currency using many ways , best one is Fixture or Admin panel.

7# docker file is present for the Django server , Redis and Postgres.

although i haven't used postgrest insted used default Sqlite as it is dummy project.

