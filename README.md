# Address Validation

This project validates addresses against PIN codes using the India Postal API.

## Usage

The `validate_address` function takes an address and PIN code, calls the API to validate, and returns True if valid:

```python
validate_address(address, pincode)

# sample usage
addresses = [
"Address 1",
"Address 2"  
]

pincodes = ["110001", "110002"]

for address, pincode in zip(addresses, pincodes):
print(validate_address(address, pincode))

 Here is a sample README.md file for this project:

```markdown
# Address Validation

This project validates addresses against PIN codes using the India Postal API.

## Usage

The `validate_address` function takes an address and PIN code, calls the API to validate, and returns True if valid:

```python
validate_address(address, pincode)
```

Sample usage:

```python
addresses = [
  "Address 1",
  "Address 2"  
]

pincodes = ["110001", "110002"]

for address, pincode in zip(addresses, pincodes):
  print(validate_address(address, pincode)) 

## Requirements

- requests
- API key from [India Postal API](https://www.postalpincode.in/Api-Details)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
