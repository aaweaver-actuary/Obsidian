#nodejs #npm 

### install #axios:
```js
npm init // get the package.json
npm install axios // download from #npm-registry 
```

### add it to a script:
```js
// put this at the top of the script:
const axios = require('axios');
```

### make a `GET` request
```js
axios.get('https://www.google.com') 
	.then((response) => {
		console.log(response);
	})
	.catch((err) => {
		console.log(err);
	})
	.then(() => {
		console.log("all done");
	})
```

- #axios uses #promises syntax (the `.then(() => {})`)
- 