# Card of the Day (cotd) API

Just your basic CRUD API -- get a card of the day, save some text with one, see a list of all your cards.

## Requirements

- Node/NPM

- the AWS CLI

- the Serverless CLI

- (Easily optional) - your own domain and an AWS certificate for the domain or wildcard subdomain

## Setup

```bash
npm install
```

## Deployment

Take note of `.env.example`. You'll want to supply a custom domain using this and rename it to `.env`.

Once you have that `.env` file:

```bash
serverless create_domain --profile=XXX
```

In order to deploy the endpoints, simply run:

```bash
serverless deploy --profile=XXX
```

## Usage

You can create, retrieve, update, or delete scans with the following commands:

### Create a cotd

```bash
curl -X POST <your CREATE endpoint> -H "x-api-key: XXX"
```


### Update a cotd

```bash
curl -X POST <your UPDATE endpoint> -H "x-api-key: XXX" --data "{ ""text"": ""This is a note for this card."" }"
```

### Get one/all cotd

```bash
curl <your GET endpoint> -H "x-api-key: XXX"
curl <your GET ALL endpoint> -H "x-api-key: XXX"
```

### Delete a cotd

```bash
curl <your DELETE endpoint> -H "x-api-key: XXX"
```

## Teardown

You'll want to run

```bash
serverless remove --profile=XXX
```

And don't forget to manually delete the custom domain in APIGateway and the A and AAAA records in Route 53