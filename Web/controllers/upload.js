const express = require('express')
const multer = require('multer')
const upload = multer({ dest: 'uploads/' })


exports.upload = (req, res) => {
    res.send(JSON.stringify({ok: true}))
};
