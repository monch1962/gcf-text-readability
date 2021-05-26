# gcf-text-readability
Google Cloud Function to check text readability

## To deploy

`$ ./gcf-deploy.sh`

## To use

Send it a http POST with a JSON payload such as 
`
{
    "text": "This is the text I would like you to check for me
}
`

and you should get a response back. The `readability` number in the response corresponds to years of education, so a '9.0' would indicate year 9 of education