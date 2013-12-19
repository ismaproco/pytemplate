pytemplate
==========

Simple folder and file template generator in python 2.7.

just call the script with the template file as a parameter or just save your template as template.tf the "tf" extension is optional.

```
pytemplate.py mytemplate.tf
```
or 
```
pytemplate.py mytemplate.tf
```

==========
The Template
------------

You just need to create a template with the custom grammar as follow:

* Braces {} let you define a list of files.
* Square [] bracket let you define a list of folders.

For example if the file has the following grammar:
```
{index.html,contact.html, aboutus.html }
```
It will create those empty files.

Or if instead is:
```
[main, imgs, libs, data]
```
It will create those empty folders.

but can also combine them and create more complex templates
```
[imgs]
[libs[jquery{jquery.min.js,jquery.min.ui.js},mootols{mootols.js},data]]
[docs]
[views]
```

you can check the template.tf file included in the repository for a real case mid-complex template.

by: @ismapro
