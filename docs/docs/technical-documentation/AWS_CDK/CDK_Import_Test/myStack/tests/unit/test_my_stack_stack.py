import aws_cdk as core
import aws_cdk.assertions as assertions

from my_stack.my_stack_stack import MyStackStack


# example tests. To run these tests, uncomment this file along with the example
# resource in my_stack/my_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyStackStack(app, "my-stack")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
