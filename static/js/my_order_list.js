var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var MyOrdersApp = require('./MyOrdersApp/OrdersApp');
var OrderDetailApp = require('./MyOrdersApp/OrderDetailApp');
var PayApp = require('./PayApp/PayApp');
var OrderComplain = require('./MyOrdersApp/OrderComplainApp');
var payConfirm = require('./PayApp/payConfirm');


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
    <DefaultRoute handler={MyOrdersApp}/>
    <Route name="order" path=":oid" handler={OrderDetailApp} />
    <Route name="pay" path=":oid/pay" handler={PayApp} />
    <Route name="complain" path=":oid/complain" handler={OrderComplain} />
    <Route name="payConfirm" path=":oid/payConfirm" handler={payConfirm} />
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
