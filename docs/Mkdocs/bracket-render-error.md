# How to resolve the Macro Rendering Error

When putting things in a `{}` bracket within a YAML codeblock you get the error `jinja2.exceptions.UndefinedError: 'xxxxxx' is undefined`.

The easiest way to output a literal variable delimiter is by using a variable expression, for example:

```YAML
run: git push --mirror https://x-token-auth:${{ '{{ secrets.AUTH_TOKEN }}' }}@bitbucket.org/workspace/repository.git
```

["Escaping in Jinja"](https://jinja.palletsprojects.com/en/3.1.x/templates/#escaping)
