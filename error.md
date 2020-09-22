## Error: with streamlit caching
Running your code, results in the following error -

```python
UnhashableTypeError: Cannot hash object of type tensorflow.python.util.object_identity._ObjectIdentityWrapper, found in the return value of get_qa_pipeline().

While caching the return value of get_qa_pipeline(), Streamlit encountered an object of type tensorflow.python.util.object_identity._ObjectIdentityWrapper, which it does not know how to hash.

To address this, please try helping Streamlit understand how to hash that type by passing the hash_funcs argument into @st.cache. For example:

@st.cache(hash_funcs={tensorflow.python.util.object_identity._ObjectIdentityWrapper: my_hash_func})
def my_func(...):
    ...

If you don't know where the object of type tensorflow.python.util.object_identity._ObjectIdentityWrapper is coming from, try looking at the hash chain below for an object that you do recognize, then pass that to hash_funcs instead:
```
![error](resources/error.png)

This error occurs when using streamlit caching.

I know this is not a very good way to report bugs :( Should have created an issue instead.