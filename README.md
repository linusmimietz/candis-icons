# Candis Icons

TBD

## Limitations

This approach assumes that SVG files are relatively simple and contain only 'path' elements. If your SVG files contain other types of elements, like 'circle', 'rect', 'text', etc., we may need to enhance the Python script to handle those.

Additionally, we should add error handling to the Python script to make it more robust. Currently, the script does not handle cases where an SVG file is not well-formed or does not contain any 'path' elements, which might cause exceptions at runtime.

This approach also assumes that any time a pull request is merged, it may contain changes to the SVG files and thus the spritemap needs to be regenerated. If in our workflow, SVG changes are infrequent, you might want to modify the trigger for this action, or add a condition to check whether any SVG files were actually changed before running the Python script.

## ToDo

-   rename path properties to camelcase
-   add “Conventional commits” message formatting
