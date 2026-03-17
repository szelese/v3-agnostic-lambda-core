FROM public.ecr.aws/lambda/python:3.12

# Dependencies, changed infrequently=top layer
COPY requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt
RUN pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Source code, changed frequently=bottom layer
COPY src/agnostic_lambda_core ${LAMBDA_TASK_ROOT}/agnostic_lambda_core

# Handler function, defined in src/agnostic_lambda_core/main.py
CMD ["agnostic_lambda_core.main.handler"]