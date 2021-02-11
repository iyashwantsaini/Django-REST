# DJANGO-REST

Basic REST-API
- Serializers
- Function based views
- Class based views
- Generic Views
- Authentication
- ViewSets
- Generic ViewSets

### Superuser
- uname=> user 
- passw=> user
- auth-token=> 270801e49bafecbfdaf813f690b7c36a81e5eff7

### Basic Auth
- js-fetch()
```
var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic dXNlcjp1c2Vy");
var raw = "";

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8000/generic/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
- node-axios
```
var axios = require('axios');
var data = '';

var config = {
  method: 'get',
  url: 'http://127.0.0.1:8000/generic/',
  headers: { 
    'Authorization': 'Basic dXNlcjp1c2Vy'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});

```
- python-request
```
import requests
url = "http://127.0.0.1:8000/generic/"
payload={}
headers = {
  'Authorization': 'Basic dXNlcjp1c2Vy'
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
```

### Token-Auth
- js-fetch()
```
myHeaders.append("Authorization", "Token 270801e49bafecbfdaf813f690b7c36a81e5eff7");
```
- node-axios
```
headers: { 
  'Authorization': 'Token 270801e49bafecbfdaf813f690b7c36a81e5eff7'
},
```
- python-request
```
headers = {
  'Authorization': 'Token 270801e49bafecbfdaf813f690b7c36a81e5eff7'
}
```

views read: down-up

## License

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

By [Yashwant](https://github.com/meyash)

## Contributors

<img src="https://avatars3.githubusercontent.com/u/21121279?s=460&u=f0450278b2b569c4443ab8ee03f9dff7015da5bf&v=4" width="100px;" alt="toofff"/><br />

<a href="https://meyash.xyz/" style="margin-right:30px;"><img src="https://meyash.xyz/assets/icons/siteicon.png" width="25"></a>
<a href="https://meyash.xyz/resume.pdf" style="margin-right:30px;"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/libreoffice.svg" width="25"></a> 
<a href="https://www.linkedin.com/in/meyash21/" style="margin-right:30px;"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" width="25"></a>
<a href="https://twitter.com/meyash21" style="margin-right:30px;"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" width="25"></a>
<a href="https://www.codechef.com/users/meyash21" style="margin-right:30px;"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/codechef.svg" width="25"></a>  