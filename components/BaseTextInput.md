---
defines-react-components: true
---

[input - MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text)

```jsx:component:BaseTextInput
  // this component returns a text input
  // if you want 

  const type = props.type || 'text';
  const placeholder = props.placeholder || 'Enter text...';
  const className = props.className || 'default-input';
  const onChange = props.onChange || (() => {});
  const onBlur = props.onBlur || (() => {});
  // const autoFocus = props.autoFocus || false;
  // const disabled = props.disabled || false;
  const maxLength = props.maxLength;
  const minLength = props.minLength;



  return (
    <input
      type={type}
      name={props.name}
      placeholder={placeholder}
      className={`${className} base-text-input`}
      onChange={onChange}
      onBlur={onBlur}
      // autoFocus={autoFocus}
      // disabled={disabled}
      maxLength={maxLength}
      minLength={minLength}
      {...props.otherProps}
    />
  );
```

`jsx:<BaseTextInput />`
