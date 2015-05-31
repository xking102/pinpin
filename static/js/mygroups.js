var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var MyGroupsApp = require('./MyGroup/GroupsApp');



var App = React.createClass({

  contextTypes: {
    router: React.PropTypes.func.isRequired
  },
  render: function () {
    var params = this.context.router.getCurrentParams();
    console.log(this.context.router.getCurrentRoutes()[1].name);
    var oid = params.oid;
    return (
      <div>
          <RouteHandler oid={oid}/>
      </div>
    );
  }
});




var routes = (
  <Route handler={App}>
    <DefaultRoute handler={MyGroupsApp}/>
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
