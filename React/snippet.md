#

```
import React from 'react';

function ${TM_FILENAME_BASE}() {
  return (
    <div>
      Hello React!
    </div>
  );
}

export default ${TM_FILENAME_BASE};
```

->

```
{
    "React Functional Component": {
  "prefix": "fc",
  "body": [
    "import React from 'react';",
    "",
    "export default function ${TM_FILENAME_BASE}() {",
    "  return (",
    "    <div>",
    "      Hello React!",
    "    </div>",
    "  );",
    "}",
    "",
  ],
  "description": "React Functional Component"
}
}
```