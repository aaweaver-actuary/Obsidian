---
defines-react-components: true
---
```jsx:component:Input
return (<input
		id="name-input"
		type="text"
		placeholder="Andy"
		value={props.name}
		onChange={props.onChange}/>)
```
```jsx:component:Hello
	return <h1>HELLO</h1>;
```

```jsx:component:App
const [name, setName] = React.useState('Andy');
return (
	<>
		<Input name={name} onChange={() => setName(name)} />
		<Hello />
	</>
	);
```
```jsx:
<App />
```
