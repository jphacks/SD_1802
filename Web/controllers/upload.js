const fs = require('fs');

exports.upload = (req, res) => {
    // change file name for user name
    fs.rename('uploads/tmp.jpg', 'uploads/' + req.user['profile']['name'] + '.jpg', function(err){});

    req.flash('success', {msg: 'File was uploaded successfully.'});
    res.redirect('/account');
};

exports.getFileUpload = (req, res) => {
    res.redirect('/account');
};