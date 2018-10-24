/**
 * GET /
 * Home page.
 */
exports.index = (req, res) => {
  if(req.user){
    res.render('index',{
      title: 'Index'
    });
  } else {
    res.render('home', {
      title: 'Home'
    });
  }
};
