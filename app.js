// functions/app.js
const express = require('express');
const app = express();

app.use(express.static('templates'));

app.get('*', (req, res) => {
    res.sendFile('index.html', { root: 'templates' });
});

const PORT = process.env.PORT || 8888;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
