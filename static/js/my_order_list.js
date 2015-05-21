var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var MyOrdersApp = require('./MyOrdersApp/OrdersApp');
var OrderDetailApp = require('./MyOrdersApp/OrderDetailApp');

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
    <DefaultRoute handler={MyOrdersApp}/>
    <Route name="order" path="order/:oid" handler={OrderDetailApp} />
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
