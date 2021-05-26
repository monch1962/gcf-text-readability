#!/bin/bash
gcloud functions deploy text-readability --entry-point evaluate_text --runtime python39 --trigger-http --allow-unauthenticated
