package com.myorg;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.cloudformation.include.CfnInclude;
import software.constructs.Construct;

public class HelloCdkCfnStack extends Stack {
    public HelloCdkCfnStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public HelloCdkCfnStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        CfnInclude template = CfnInclude.Builder.create(this, "Template")
        	.templateFile("my-template.json")
        	.build();
    }
}
