# Quick Reference Guide

## Project Components

### Files Structure
```
main.py              # Main application (entry point)
requirements.txt     # Dependencies
API_DOCUMENTATION.md # Comprehensive documentation
QUICK_REFERENCE.md   # This quick reference
```

## Public APIs & Functions

### 1. main() Function
```python
def main()
```
- **Purpose**: Entry point for the Streamlit application
- **Location**: `main.py:29`
- **Usage**: Automatically called when running `streamlit run main.py`
- **Returns**: None

### 2. Streamlit Components Used

#### st.title()
```python
st.title('HELLO STREAMLIT')
```
- **Purpose**: Displays main application title
- **Location**: `main.py:41`
- **Parameter**: String (the title text)
- **Output**: H1 heading in the web interface

## Quick Commands

### Installation
```bash
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run main.py
```

### Access Application
- URL: `http://localhost:8501`
- Default port: 8501

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | latest | Web app framework |

## Common Streamlit Components Reference

### Text Elements
```python
st.title('Title')           # H1 heading
st.header('Header')         # H2 heading  
st.subheader('Subheader')   # H3 heading
st.text('Fixed text')       # Monospace text
st.markdown('**Bold**')     # Markdown support
st.write('Any content')     # Universal display
```

### Input Widgets
```python
st.button('Click me')
st.checkbox('Check this')
st.radio('Choose', ['A', 'B'])
st.selectbox('Select', ['X', 'Y'])
st.slider('Slide', 0, 100, 50)
st.text_input('Enter text')
st.text_area('Long text')
```

### Data Display
```python
st.dataframe(df)            # Interactive table
st.table(df)                # Static table
st.json(data)               # JSON display
st.code(code_string)        # Code block
```

### Charts
```python
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)
```

### Layout
```python
st.sidebar.title('Side')    # Sidebar content
st.columns(2)               # Multi-column layout
st.expander('Expand')       # Collapsible section
```

## Configuration Options

### Command Line
```bash
streamlit run main.py --server.port 8502
streamlit run main.py --server.address 0.0.0.0
streamlit run main.py --server.headless
```

### Environment Variables
```bash
export STREAMLIT_SERVER_PORT=8502
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## Development Workflow

1. **Edit** `main.py`
2. **Save** changes
3. **Reload** browser (auto-refresh enabled)
4. **Test** functionality

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | `pip install streamlit` |
| Port in use | Use `--server.port XXXX` |
| App not loading | Check Python installation |
| Syntax error | Validate Python code |

## Next Steps

Add these components to extend functionality:
- User inputs (text, buttons, sliders)
- Data visualization (charts, graphs)
- File upload capabilities
- Database connections
- Authentication systems

---

*For detailed documentation, see `API_DOCUMENTATION.md`*