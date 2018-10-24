const fs = require('fs');

exports.upload = (req, res) => {
    // change file name for user name
    var path = 'uploads/' + req.user['profile']['name'];
    // if (!fs.existsSync(path)) {
    //     fs.mkdirSync(path);
    // }
    fs.rename('uploads/tmp.jpg', path + '.jpg', function(err){});

    req.flash('success', {msg: 'File was uploaded successfully.'});
    res.redirect('/account');
};

exports.getFileUpload = (req, res) => {
    res.redirect('/account');
};