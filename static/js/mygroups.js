var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var GroupsApp = require('./MyGroup/GroupsApp');
var UploadCheckFiles = require('./Mygroup/UploadCheckFiles');

var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');



injectTapEventPlugin();
var App = React.createClass({
  childContextTypes: {
      muiTheme: React.PropTypes.object
    },
    getChildContext: function() {
      return {
        muiTheme: ThemeManager.getCurrentTheme()
      };
  },
  contextTypes: {
    router: React.PropTypes.func.isRequired
  },

  render: function () {
    return (
      <div>
          <RouteHandler/>
      </div>
    );
  }
});




var routes = (
  <Route handler={App}>
    <DefaultRoute handler={GroupsApp}/>
    <Route name="Upload" path=":gid/check" handler={UploadCheckFiles} />
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
