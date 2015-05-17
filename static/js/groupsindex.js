var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var GroupsApp = require('./GroupsApp/GroupsApp');
var GroupApp = require('./GroupApp/GroupApp');

var App = React.createClass({

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
    <Route name="group" path="group/:gid" handler={GroupApp} />
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
