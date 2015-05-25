var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var UserInfoApp = require('./UserApp/UserInfoApp');
var UserAddressApp = require('./UserApp/UserAddressApp');
var UserPassword = require('./UserApp/UserPassword');



var App = React.createClass({

  contextTypes: {
    router: React.PropTypes.func.isRequired
  },
  listUser:function(){
    $.ajax({
      url      : '/api/v1/user',
      dataType : 'json',
      type     : 'GET',
      success: function(resp) {
        this.setState({
          user:resp.user
        });
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
      }.bind(this)
    });
  },

  getInitialState:function(){
    return {
      user: []
    }
  },
  componentDidMount:function(){
    this.listUser();
  },
  render: function () {
    var params = this.context.router.getCurrentParams();
    console.log(this.context.router.getCurrentRoutes()[1].name);
    var oid = params.oid;
    return (
      <div>
          <RouteHandler user={this.state.user}/>
      </div>
    );
  }
});




var routes = (
  <Route handler={App}>
    <DefaultRoute handler={UserInfoApp}/>
    <Route name="address" path="address" handler={UserAddressApp} />
    <Route name="password" path="password" handler={UserPassword} />
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
