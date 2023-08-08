def main():
    # Get input from the user
    html_code = input("Enter HTML code:\n")
    css_code = input("Enter CSS code:\n")
    js_code = input("Enter JavaScript code:\n")

    # Create the merged code
    merged_code = f'''
<!DOCTYPE html>
<html>
<head>
<style>
{css_code}
</style>
</head>
<body>
{html_code}
<script>
{js_code}
</script>
</body>
</html>
'''

    # Output the merged code
    print("\nMerged Code:")
    print(merged_code)

if __name__ == "__main__":
    main()
