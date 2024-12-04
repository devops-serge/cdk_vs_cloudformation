# The AWS CDK v2 Installation

1. Install Node.js

- Download and install from [Node.js official site](https://nodejs.org/en/download/package-manager).
- check the installation
```shell
node --version
```

2. Set Up AWS CLI
- Install: [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Create an access keys using AWS IAM
- Configure:
```shell
aws configure
```

3. Install the AWS CDK
```shell
npm install -g aws-cdk
cdk --version
```

4. Install the preferred language. For example, [Python](https://www.python.org/downloads/) >= 3.6.

5. Create a structure of files and folders within an empty directory
```shell
mkdir my_example_app && cd my_example_app
cdk init app --language python
```

6. Create a `virtualenv`
```shell
python3 -m venv .venv
```

7. Activate your `virtualenv`
```shell
source .venv/bin/activate
```

8. Install the required dependencies
```shell
pip install -r requirements.txt
```

9. Add your code





