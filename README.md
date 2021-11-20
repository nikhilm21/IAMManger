# IAMManger

To deploy the code on your AWS SAM:

1. Ensure that the AWS CLI is set-up.
2. Run the commands below to set-up SAM and deploy it. 
      ```
      git init
      git add .
      sam build
      sam deploy --guided
      ```
 Note: The default config file is already there, so you can skip through the process of selecting server and DBName.
