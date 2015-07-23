var React = require("react");

var mui = require('material-ui');
var {TextField, Paper, RaisedButton, Snackbar} = mui;
var Dropzone = require('react-dropzone');
var LoadingMask = require("../Components/LoadingMask");


module.exports = React.createClass({
    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    _checkField:function(){

        var errorImages = this.state.errorImages;

        if(errorImages.length>0){
          this.setState({
            errorSubmit:'请填写完整'
          });
          return true;
        }else{
          this.setState({
            errorSubmit:''
          });
          return false;
        }
    },
    PostFiles:function(num){
        var params = this.context.router.getCurrentParams();
        var gid = params.gid;
        if(num){
          return '';
        }
        this.setState({
          submitflag:true
        });
        this.refs.loading.show();
        var formData = new FormData();
        for (var i=0;i<this.state.images.length;i++){
          var file = this.state.images[i];
          formData.append('photos',file);
        }
        formData.append('images',this.state.images);
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        console.log(csrftoken);
            $.ajaxSetup({
              beforeSend: function(xhr, settings) {
                  if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                      xhr.setRequestHeader("X-CSRFToken", csrftoken);
                  }
            }
        });
        $.ajax({
          url      : '/groups/check/' + gid,
          type     : 'POST',
          dataType: 'json',
          cache: false,
          contentType: false,
          processData: false,
          data:formData,
          success: function(resp) {
            console.log('succ');
            this._onHandleCancel();
            this.refs.loading.dismiss();
            this.setState({
              submitflag:false
            });
            this.refs.snackbar_succ.show();
            this.context.router.transitionTo('main');
          }.bind(this),

          error: function(xhr, status, err) {
            console.error(status, err.toString);
            this.setState({
              submitflag:false
            });
            this.refs.loading.dismiss();
          }.bind(this)
        });
    },
    getInitialState:function(){
      return {
        images:[],
        flag:true,
        errorImages:'别忘了上传图片',
        errorSubmit:'',
        submitflag:false,
      }
    },
    _handleForm:function(e){
      e.preventDefault();
      var num = this._checkField();
      this.PostFiles(num);
    },



    render: function () {
      var showSubmitError = this.state.errorSubmit.length==0?'':
      <div style={{marginTop:'50px'}} className="alert alert-error">{this.state.errorSubmit}</div>;
      return (
        <div style={{marginLeft:'20%',marginRight:'20%'}}  >
            <Paper zDepth={3}>
            <div style={{marginLeft:'10px',marginRight:'10px',paddingBottom:'20px'}}>


            <form  onSubmit={this._handleForm} ref="addGroupForm" name="addGroup" encType="multipart/form-data" method="POST">


              <br/>

              <Dropzone ref="dropzone" onDrop={this._onDrop} size={150} >
                <div>你可以拖拽多张图片到此处或者双击选择多张图片</div>
              </Dropzone>
              {this.showFiles()}

              <br/>


              <div className="pull-right">
              <a className="btn btn-link" onClick={this._onHandleCancel}>重新填写</a>
              &nbsp;
              <RaisedButton
              label="添加"
              secondary={true}
              disabled={this.state.submitflag}
              />



               <Snackbar
                  ref="snackbar_succ"
                  message={'发布成功'}
              />

              </div>

              {showSubmitError}


            </form>


            </div>
            </Paper>
            <LoadingMask ref="loading"/>
        </div>
      );
    },

    _checkimage:function(img){
      if(img.size>1024*1024&&img.type in ('image/jpeg','image/gif','image/png')){
        return false;
      }{
        return true;
      }
    },

    _onDrop:function(imgs){
      if(imgs.length<6){
        var imgslist=[];
        for (var i=0;i<imgs.length;i++){
          if(this._checkimage(imgs[i])){
            imgslist.push(imgs[i]);
          }
        }
        this.setState({
          images:imgslist,
          errorImages:''
        });
      }else{
        this.setState({
          images:'',
          errorImages:'至多可以上传5张图片'
        });
      }
    },

    showFiles: function () {
      if (this.state.images.length <= 0) {
        return <div style={{marginTop:'10px'}} className="alert alert-error">{this.state.errorImages}</div>;
      }

      var images = this.state.images;

      return (
        <div>
          <h3>预览</h3>
            {[].map.call(images, function (f, i) {
              return <img style={{marginRight:'3px',marginBottom:'3px'}}width={100} height={100} key={i} src={f.preview} />;
            })}
        </div>
      );
    },



  _onHandleCancel:function(){
    this.refs.addGroupForm.getDOMNode().reset();
    this.setState({
      images:[],
      errorImages:'别忘了上传图片',
      errorSubmit:''
    })
  },




})
